#ifndef CHUNK_H
#define CHUNK_H

#include <string>

#include "element.h"

class Chunk : public Element<std::string, int> {
private:

public:
  Chunk();
  Chunk(std::string name);

  ~Chunk();

  std::string getName();
  int getFrequency();

  void incrementFrequency();
};

#endif //CHUNK_H
