#ifndef CHUNK_H
#define CHUNK_H

#include <string>

#include "element.h"

class Chunk : Element<std::string, int> {
private:

public:
  Chunk();
  Chunk(std::string name);

  ~Chunk();

  std::string getName();
  int getFrequency();
};

#endif //CHUNK_H
