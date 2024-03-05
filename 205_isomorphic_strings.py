class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
      if len(s) != len(t):
          return False

      s_to_t_mapping = {}
      t_seen = set()

      for char_s, char_t in zip(s, t):
          if char_s in s_to_t_mapping:
              if s_to_t_mapping[char_s] != char_t:
                  return False
          else:
              if char_t in t_seen:
                  return False
              s_to_t_mapping[char_s] = char_t
              t_seen.add(char_t)

      return True



#THis is solution is the real good solution near to out concept and implementation of the question
