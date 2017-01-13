#include "chunkList.h"

ChunkList::ChunkList() : Row() {}

ChunkList::ChunkList(Chunk chunk) : Row(chunk) {}

Chunk& ChunkList::getChunk() {
  return Row::getPrimary();
}

std::vector<Chunk> ChunkList::getPhonemes() {
  return Row::getColumns();
}

int ChunkList::addPhoneme(Chunk phoneme) {
  return Row::addElement(phoneme);
}
