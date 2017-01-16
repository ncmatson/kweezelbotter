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
