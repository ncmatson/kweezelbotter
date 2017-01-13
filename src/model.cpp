#include "model.h"
#include <iostream>
Model::Model() : Matrix() {}

void Model::addChunkPhonemePair(Chunk chunk, Chunk phoneme) {
  int chunkIndex = Matrix::findRow(ChunkList(chunk));

  // add if not found
  if (chunkIndex == rows.size()){
    Matrix::addRow(ChunkList(chunk));
  }
  // increment the freq of added chunk
  rows[chunkIndex].getChunk().incrementFrequency();

  // add the phoneme (or find its existing index)
  int phonemeIndex = rows[chunkIndex].addPhoneme(phoneme);
  rows[chunkIndex][phonemeIndex].incrementFrequency();
}
