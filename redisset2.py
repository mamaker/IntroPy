# -*- coding: utf-8 -*-
"""
redisset2.py
Created on Wed Apr 17 13:36:59 2019

@author: madhu
"""

import redis

# Create a redis client
redisClient = redis.StrictRedis(host='localhost',
                                port=6379,
                                db=0)
# Name of the Redis sorted set
players = "Players"
# Add a player to the Redis sorted set against the score
score       = 56
playerName  = "Player1"
redisClient.zadd(players, score, playerName)
# Add a player to the Redis sorted set against the score
score       = 25
playerName  = "Player2"
redisClient.zadd(players, score, playerName)
# Add a player to the Redis sorted set against the score
score       = 37
playerName  = "Player3"
redisClient.zadd(players, score, playerName)
# Print all the players based on the score in ascending order
print("Contents of the Redis sorted set in ascending order:")
print(redisClient.zrange(players, 0, -1))
# Print all the players based on score in descending order
print("Contents of the Redis sorted set in descending order:")
print(redisClient.zrange(players, 0, -1, desc=True))
# Print all the players based on score in descending order along with the scores 
print("Contents of the Redis sorted set with scores:")
print(redisClient.zrange(players, 0, -1, withscores=True))
