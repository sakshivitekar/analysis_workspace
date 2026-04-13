
-- Activation Funnel SQL Queries



-- 1️⃣ DAILY SIGNUPS

-- Counts number of users signed up per day

SELECT 
    DATE(signup_date) AS signup_day,
    COUNT(user_id) AS total_signups
FROM users
GROUP BY signup_day
ORDER BY signup_day;


-- 2️⃣ DAILY ACTIVE USERS (DAU)

-- Users who performed any event per day

SELECT 
    DATE(event_time) AS activity_day,
    COUNT(DISTINCT user_id) AS daily_active_users
FROM events
GROUP BY activity_day
ORDER BY activity_day;


-- 3️⃣ ACTIVATION WITHIN 24 HOURS

-- Users who performed key action (apply/post) within 24 hrs of signup

SELECT 
    COUNT(DISTINCT u.user_id) AS activated_users_24h
FROM users u
JOIN events e 
    ON u.user_id = e.user_id
WHERE 
    e.event_time <= u.signup_date + INTERVAL '24 HOURS'
    AND e.event_type IN ('apply', 'post_created');


-- 4️⃣ ACTIVATION RATE (24h)

-- % of users activated within 24 hrs

SELECT 
    COUNT(DISTINCT e.user_id) * 100.0 / COUNT(DISTINCT u.user_id) AS activation_rate_24h
FROM users u
LEFT JOIN events e 
    ON u.user_id = e.user_id
    AND e.event_time <= u.signup_date + INTERVAL '24 HOURS'
    AND e.event_type IN ('apply', 'post_created');


-- 5️⃣ TOP EVENTS

-- Most frequent user actions

SELECT 
    event_type,
    COUNT(*) AS total_events
FROM events
GROUP BY event_type
ORDER BY total_events DESC;


-- 6️⃣ USERS BY ROLE

-- Distribution of users by role

SELECT 
    role,
    COUNT(user_id) AS total_users
FROM users
GROUP BY role;


-- 7️⃣ USERS BY COLLEGE

-- Distribution of users by college

SELECT 
    college,
    COUNT(user_id) AS total_users
FROM users
GROUP BY college
ORDER BY total_users DESC;

