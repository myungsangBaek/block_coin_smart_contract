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

    # 객체의 변수를 사용하기에 self 필요
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

# Mining Blockchain
    def get_previous_block(self):
        return self.chain[-1]
