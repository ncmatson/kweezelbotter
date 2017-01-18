class Utils:

    @staticmethod
    def flatten(l):
        flat_list = []
        for el in l:
            if isinstance(el, (list, tuple)):
                for j in Utils.flatten(el):
                    flat_list.append(j)
            else:
                flat_list.append(el)

        return flat_list

    @staticmethod
    def max_by_length(s1, s2):
        if len(s1) > len(s2):
            return s1, s2
        else:
            return s2, s1
