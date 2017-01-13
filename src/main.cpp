#include <iostream>

#include "model.h"

int main() {

  Chunk chunk("K");
  Chunk phoneme("k");

  Model model;

  model.addChunkPhonemePair(chunk, phoneme);

  std::cout<<model[0].getChunk().getFrequency()<<std::endl;

}
