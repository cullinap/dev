#include <ctime>
#include <vector>


using namespace std;

// transaction data
struct TransactionData {
	double amount;
	string senderKey;
	string receiverKey;
	time_t timestamp
}


// Block Class
class Block {
	private:
		int index;
		size_t blockHash;
		size_t previousHash;
		size_t generateHash();

	public:
		// Constructor
		block(int idx, TransactionData d, size_t prevHas);

		// Get Original Hash
		size_t getHash();

		// Get Previous Hash
		size_t getPreviousHash();

		// Transaction Data
		TransactionData data;

		// Validate Has
		bool isHashValid();
		
}

Block::Block(int idx, TransactionData d, size_t prevHash) {
	index = idx;
	data = d;
	previousHash = prevHash;
	blockHash = generateHash();
}

// private fns
size_t Block::generateHash() {
	hash<string> hash1;
	hash<size_t> hash2;
	hash<size_t> finalHash;
	string toHash = to_string(data.amount) + data.receiveKey + data.senderKey + to_string(data.timestamp);

	return finalHash(hash1(toHash) + hash2(previousHash));
};

// public fns
size_t Block::getHash() {
	return blockHash;
}

size_t Block::getPreviousHash() {
	return previousHash;
}

bool Block::isHashValid() {
	return generateHash() == blockHash;
}

// blockchain
class Blockchain {

	private:
		Block createGenesisBlock();
		
	public:
		vector<Block> chain;

		// Constructor
		Blockchain();

		// Public functions
		void addBlock(TransactionData data);
		void isChainValid();

		// Contrived Example for demo only!!
		Block *getLatestBlock();

}












