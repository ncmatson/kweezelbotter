#ifndef MODEL_H
#define MODEL_H

#include "matrix.h"
#include "chunkList.h"

class Model : public Matrix<ChunkList> {
public:
  Model();

  void addChunkPhonemePair(Chunk chunk, Chunk phoneme);
};

#endif //MODEL_H
