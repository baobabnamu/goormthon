require('dotenv').config();
const express = require('express');
const mysql = require('mysql2/promise');
const { createClient } = require('redis');

const app = express();
const port = process.env.PORT || 3000;

// MySQL connection pool
const pool = mysql.createPool({
  host: process.env.MYSQL_HOST || 'mysql',
  port: process.env.MYSQL_PORT || 3306,
  user: process.env.MYSQL_USER || 'testuser',
  password: process.env.MYSQL_PASSWORD || 'testpass',
  database: process.env.MYSQL_DATABASE || 'testdb',
});

// Redis client
const redisClient = createClient({
  socket: {
    host: process.env.REDIS_HOST || 'redis',
    port: process.env.REDIS_PORT || 6379,
  }
});

redisClient.on('error', (err) => console.error('Redis Client Error', err));

async function init() {
  try {
    // Redis 연결 테스트
    await redisClient.connect();
    console.log('Connected to Redis');

    // MySQL 연결 테스트
    const connection = await pool.getConnection();
    console.log('Connected to MySQL');
    connection.release();
  } catch (error) {
    console.error('Error connecting to database services:', error);
    process.exit(1);
  }
}

app.get('/', async (req, res) => {
  try {
    // MySQL: 현재 시간 조회
    const [rows] = await pool.query('SELECT NOW() as now');
    const mysqlTime = rows[0].now;

    // Redis: 카운터 증가
    const counter = await redisClient.incr('counter');

    res.send({
      message: 'Hello from Express!',
      mysqlTime,
      counter
    });
  } catch (error) {
    console.error('Error handling request:', error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

init().then(() => {
  app.listen(port, () => {
    console.log(`Express server running on port ${port}`);
  });
});