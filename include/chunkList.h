#ifndef CHUNK_LIST_H
#define CHUNK_LIST_H

#include "row.h"
#include "chunk.h"

class ChunkList : Row<Chunk> {
public:
  ChunkList();
  ChunkList(Chunk chunk);

  Chunk getChunk();
  std::vector<Chunk> getPhonemes();


};

#endif //CHUNK_LIST_H
