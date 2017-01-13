#ifndef CHUNK_LIST_H
#define CHUNK_LIST_H

#include "row.h"
#include "chunk.h"

class ChunkList : public Row<Chunk> {
public:
  ChunkList();
  ChunkList(Chunk chunk);

  Chunk& getChunk();
  std::vector<Chunk> getPhonemes();

  int addPhoneme(Chunk phoneme);

};

#endif //CHUNK_LIST_H
