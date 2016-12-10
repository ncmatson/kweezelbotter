/* Kweezelbotter is a pronunciation tool to pronounce
 * words like Kweezelbotter.
 *
 * Cameron Matson
 * Clayton Gentry
 * 2016
 */

#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

#include "chunkModel.h"

#define DICTIONARY_FILE "dict/dict.txt"

int bigChunks = 0;

/* splits the given string along the delimiter patern */
std::vector<std::string> split(const std::string& str, char delim) {
  std::vector<std::string> result;
  std::stringstream ss(str);
  std::string token;

  while(std::getline(ss,token,delim)) {
    result.push_back(token);
  }

  return result;
}

bool isVowel(char c) {
  switch (c) {
    case 'A':
    case 'E':
    case 'I':
    case 'O':
    case 'U': return true; break;
    default: return false;
  }
}

/* Returns the number of letters following str[i] to chunk together
 * Cases include:
 * <vowel> <vowel>
 * th
 * sh
 */
int chunkTogether(const std::string& str, int i) {
  //if the last letter -> don't chunk
  if (i == str.length() - 1) return false;

  switch (str[i]) {
    case 'A':
    case 'E':
    case 'I':
    case 'O':
    case 'U': {
      // if the next letter is a vowel -> CHUNK EM
      if (isVowel(str[i+1])) {
        // if next TWO letters are vowels ->CHUNK two of em
        if (isVowel(str[i+2])) {return 2;}
        return 1;
      }
    }
    case 'T': {
      // if the next letter is an h -> CHUNK EM
      if (str[i+1] == 'H' || str[i+1] == 'T') { return 1;}
    }
    case 'S': {
      if (str[i+1] == 'H' || str[i+1] == 'S') {return 1;}
    }
    case 'C': {
      if (str[i+1] == 'H' || str[i+1] == 'K') {return 1;}
    }
    default: return 0;
  }
}

//TODO: too many big chunks
/* Splits a word into <num> "chunks"
 * Attempts to chunk letter patterns together appropriately.
 *
 * Default behavior is to do one letter per chunk
 * If the number of chunks is one less than <num>, then the remaining letters in
 * word are placed in the final chunk.
 */
std::vector<std::string> chunk(const std::string& str, int num) {
  std::vector<std::string> result;

  //put one letter in each chunk until you only have one chunk left to fill
  int i;
  for (i = 0; i < str.length() && i < (num-1); ++i) {
    // offset is the number of letters following i that should be chunked together
    int offset = chunkTogether(str,i);
    result.push_back(str.substr(i, offset+1));
    i += offset;
  }

  //fill the last chunk wih the rest of the string
  if (i < str.length()) { result.push_back(str.substr(i)); }
  if (result[result.size()-1].length() > 2) bigChunks++;

  return result;
}

void loadTrainingSet( std::string fileName, ChunkModel* cm){
  std::ifstream file(fileName);

  if (file) {
    std::string line;

    while (std::getline(file,line)) {
      if (line.substr(0,3) == ";;;") {
        continue;
      }
      else {
        cm->addLine(line);
      }
    }
  }
  else {
    std::cerr << "Unable to load dictionary" << std::endl;
  }
}

int main() {

  ChunkModel* cm = new ChunkModel();

  loadTrainingSet(DICTIONARY_FILE, cm);

  std::cout<<cm->getSize()<<std::endl;

  cm->print("data/matrix.txt");
}
