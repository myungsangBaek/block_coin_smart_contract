# Module 1: Create a Blockchain

import datetime
# 해시 할 때 사용하는 라이브러리
import hashlib
# 블록 해시 전 인코딩을 위해
import json
# jsonify == Postman 통신 용
from flask import Flask, jsonify

# Building a Blockchain


class Blockchain:
    def __init__(self):
        # 다른 블록을 포함하는 리스트
        self.chain = []
        # 첫 블록이라 previous_hash 없음
        self.create_block(proof=1, previous_hash='0')
