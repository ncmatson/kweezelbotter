/* Extends model
 * each row is a chunk and each column is a phoneme
 */

#ifndef CHUNK_MODEL_H
#define CHUNK_MODEL_H

#include <locale>
#include <set>

#include "model.h"

class ChunkModel : public Model {
public:
  ChunkModel();

  void addLine(std::string line);
  void addChunkPhonemePair(std::string chunk, std::string phoneme);

  //this will be moved to private
  std::vector<std::vector<std::string>> chunkUnknown(std::string unknown);

private:
  std::set<int> chunkSizes;


  // checks if a string is all letters
  bool isLetters(std::string word);

  // separates a string along the given delimiter
  std::vector<std::string> split(const std::string& str, char delim);

  // checks if a letter is a vowel
  bool isVowel(char c);

  // returns the number of letters following the given index to chunk together
  int chunkTogether(const std::string& str, int i);

  // splits a words into chunks such that there are <num> chunks
  std::vector<std::string> chunk(const std::string& str, int num);

};

#endif //CHUNK_MODEL_H
