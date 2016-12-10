/* Extends model
 * each row is a chunk and each column is a phoneme
 */

#ifndef CHUNK_MODEL_H
#define CHUNK_MODEL_H

#include "model.h"

class ChunkModel : public Model {
public:
  void addLine(std::string line);
  void addChunkPhonemePair(std::string chunk, std::string phoneme);
private:
  typedef std::vector<std::vector<std::string>> matrix;

  std::vector<std::string> split(const std::string& str, char delim);

  bool isVowel(char c);
  int chunkTogether(const std::string& str, int i);
  std::vector<std::string> chunk(const std::string& str, int num);

};

#endif //CHUNK_MODEL_H
