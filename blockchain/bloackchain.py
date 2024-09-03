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

    # 이전 블럭 가져오기
    def get_previous_block(self):
        return self.chain[-1]

    # 작업 증명 함수 -  작업 증명은 채굴하기 위해 찾아내는 숫자이다.
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False,
        while check_proof is False:
            # 해시 연산 - 비대칭으로 이루어진다
            hash_operation = hashlib.sha256(
                # hexdigest - 16진수 표현
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if (hash_operation[:4] == '0000'):
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # 블록체인 유효성 검사 함수 - 이전 블록 해시확인, 블록 작업 증명 확인
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block('proof')
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# Mining Blockchain


app = Flask(__name__)

blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


#  Getting the full Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)
