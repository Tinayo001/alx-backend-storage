#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  19 12:40:00 2023

@Author: Nicanor Kyamba
"""
import functools
import uuid
from typing import Union, Callable, Optional
import redis


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called

    Args:
        method (Callable): The method to be decorated

    Returns:
        Callable: The decorated method
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper to count the number of times a method is called

        Args:
            *args (Any): The positional arguments
            **kwargs (Any): The keyword arguments

        Returns:
            Callable: The decorated method
        """
        random_key = method.__qualname__
        self._redis.incr(random_key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the number of times a method is called

    Args:
        method (Callable): The method to be decorated

    Returns:
        Callable: The decorated method
    """
    random_key = method.__qualname__
    inputs = random_key + ":inputs"
    outputs = random_key + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper to store the number of times a method is called

        Args:
            *args (Any): The positional arguments
            **kwargs (Any): The keyword arguments

        Returns:
            Callable: The decorated method
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def replay(method: Callable) -> None:
    """
    Decorator to replay the method calls

    Args:
        method (Callable): The method to be decorated

    Returns:
        Callable: The decorated method
    """
    random_key = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(random_key).decode('utf-8')
    print("{} was called {} times:".format(random_key, calls))
    inputs = cache.lrange(random_key + ":inputs", 0, -1)
    outputs = cache.lrange(random_key + ":outputs", 0, -1)
    for inputt, outputt in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     inputt.decode('utf-8'),
                                     outputt.decode('utf-8')))


class Cache:
    """Cache class to store data in redis"""
    def __init__(self):
        """Initialize class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Read from Redis and recovering original type"""
        original_data = self._redis.get(key)
        if fn:
            return fn(original_data)
        return original_data

    def get_str(self, key: str) -> str:
        """
        Automatically parametrizes Cache.data with the
        correct conversion function
        """
        original_data = self._redis.get(key)
        original_data.decode('utf-8')
        return original_data

    def get_int(self, key: str) -> int:
        """
        Automatically parametrizes Cache.data with the
        correct conversion function
        """
        original_data = self._redis.get(key)
        original_data = int(original_data)
        return original_data
