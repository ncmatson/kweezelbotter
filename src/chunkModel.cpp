/* ChunkModel implementation */

#include "chunkModel.h"



//TODO: I don't like the name of this function
void ChunkModel::addLine(std::string line) {
  std::string word;
  std::string pronunciation;

  std::vector<std::string> chunks;
  std::vector<std::string> phonemes;

  std::stringstream ss(line);

  //pick off word
  ss >> word;

  //pick of pronunciation
  ss.get();
  std::getline(ss, pronunciation);
  pronunciation = pronunciation.substr(1);

  //split phonemes
  phonemes = split(pronunciation, ' ');

  //chunk word s.t. the number of chunks = number of phonemes
  chunks = chunk(word, phonemes.size());


  //add each chunk-phoneme pair to the model
  for (int i = 0; i < chunks.size(); ++i) {
    // skip if the word contains non-letter characters
    if (!isLetters(chunks[i])) continue;

    if (chunks[i].length() > max.length()) max = chunks[i];

    addChunkPhonemePair(chunks[i], phonemes[i]);
    chunkSizes.insert(chunks[i].size());
  }
}

bool ChunkModel::isLetters(std::string word) {
  std::locale loc;

  for (int i = 0; i < word.length(); ++i) {
    if (!std::isalpha(word[i])) return false;
  }
  return true;
}

void ChunkModel::addChunkPhonemePair(std::string c, std::string p){
  Word chunk(c);
  Word phoneme(p);

  addOrUpdate(chunk);
  find(chunk)->add_leader(phoneme);

}


std::vector<std::string> ChunkModel::split(const std::string& str, char delim) {
  std::vector<std::string> result;
  std::stringstream ss(str);
  std::string token;

  while(std::getline(ss,token,delim)) {
    result.push_back(token);
  }

  return result;
}

bool ChunkModel::isVowel(char c) {
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
int ChunkModel::chunkTogether(const std::string& str, int i) {
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
std::vector<std::string> ChunkModel::chunk(const std::string& str, int num) {
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

  return result;
}
