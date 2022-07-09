import logging

logging.basicConfig(filename="listTasks.log", level=logging.DEBUG)


class ListTasks:
    """
        This class is on different tasks on list given by sudhanshu sir in five different tasks given till date.
    """

    def reverse_the_given_list(self, l):
        """
        TASK-2's task
        1 . Try to reverse a list
        :param l: input list
        :return: returns the given list in reverse order
        """
        try:
            logging.info("The given list for this operation is %s", l)
            l1 = l
            l2 = l1.reverse()
            logging.info("The output of the operation is %s", l2)
            return l2
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def access_234_in_given_list(self,l):
        """
        TASK-2's task
        2. try to access 234 out of this list
        :param l: input list
        :return: returns indexes where 234 is present in the given list except for dictionary present inside the given list
        """
        try:
            l1=[]
            logging.info("The given list for this operation is %s", l)
            for i in range(len(l)):
                if(type(l[i])==int and l[i]==234):
                    l1.append(i)
                elif(type(l[i])==list or type(l[i])==set or type(l[i])==tuple):
                    for j in range(len(l[i])):
                        if(type(l[i][j])==int and l[i][j]==234):
                            l1.append((i,j))
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def access_456_in_given_list(self,l):
        """
        TASK-2's task
        3. try to access 456 out of this list
        :param l: input list
        :return: returns indexes where 456 is present in the given list except for dictionary present inside the given list
        """
        try:
            l2=[]
            logging.info("The given list for this operation is %s", l)
            for i in range(len(l)):
                if(type(l[i])==int and l[i]==456):
                    l2.append(i)
                elif(type(l[i])==list or type(l[i])==set or type(l[i])==tuple):
                    for j in range(len(l[i])):
                        if(type(l[i][j])==int and l[i][j]==456):
                            l2.append((i,j))
            logging.info("The output of the operation is %s", l2)
            return l2
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_lists_in_given_list(self,l):
        """
        TASK-2's task
        4.Try to extract only a list collection form list l
        :param l: input list
        :return: returning a list containing all the lists present in the given list
        """
        try:
            l1=[]
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if(type(i)==list):
                    l1.append(i)
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_sudh_in_given_list(self,l):
        """
        TASK-2's task
        5 . Try to extract "sudh"
        :param l: input list
        :return: returns index sudh part present in dictionary which in turn present in the given list
        """
        try:
            l1=[]
            logging.info("The given list for this operation is %s", l)
            cnt1=0
            for i in l:
                if(type(i)==dict):
                    cnt=0
                    for k,v in i.items():
                        if(type(v)==str and v=="sudh"):
                            l1.append((cnt1,cnt))
                        cnt+=1
                cnt1+=1
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_keys_into_a_list(self,l):
        """
        TASK-2's task
        6 . Try to list all the key in dict element avaible in list
        :param l: input list
        :return: returns a list containing keys of a dictionary
        """
        try:
            l1=[]
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if(type(i)==dict):
                    l1.append(i.keys())
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_values_into_a_list(self,l):
        """
        TASK-2's task
        7 . Try to extract all the value element form dict available in list
        :param l: input list
        :return: returns a list containing values of a dictionary
        """
        try:
            l1=[]
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if(type(i)==dict):
                    l1.append(i.values())
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def List_Append(self,*l):
        """
        TASK-5's task
        replica of list append
        :param l: dynamic input of n items
        :return: returns a list of above items
        """
        logging.info("The given list for this operation is %s", l)
        n=0
        l1=[0]*len(l)
        for i in l:
            l1[n]=i
            n+=1
        logging.info("The output of the operation is %s", l1)
        return l1

    def List_Pop(self,l,index=None):
        """
        TASK-5's task
        replica of list pop
        :param l: input list
        :param index: index from which we want to pop of the element
        :return: pops out the element for the given index
        """
        logging.info("The given list for this operation is %s", l)
        if(index == None):
            logging.info("The output of the operation is %s", str(l[len(l) - 1]))
            del l[len(l) - 1]
        elif (len(l) == 0):
            logging.info("list is empty!!!")
        elif (index < 0 or index > len(l)):
            logging.info("list index out of bounds!!!")
        else:
            logging.info("The output of the operation is %s", str(l[index]))
            del l[index]

    def List_Extend(self,l,ds):
        """
        TASK-5's task
        replica of list extend
        :param l: input list
        :param ds: data structure we want to extend
        :return: returns list with extend elements of ds
        """
        try:
            logging.info("The given list for this operation is %s", l)
            if (type(ds) == list or type(ds) == tuple or type(ds) == set or type(ds) == dict or type(ds) == str):
                for i in ds:
                    l.append(i)
            logging.info("The output of the operation is %s", l)
            return l
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def filter_out_vowels(self,s):
        """
        TASK-4's task(Challenge-1)
        :param s: input string
        :return: returns a list of vowels present in the text.
        """
        try:
            logging.info("The given list for this operation is %s", s)
            vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            l = [x for x in s if x in vowels]
            logging.info("The output of the operation is %s", l)
            return l
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def concatenating_multiple_lists(self,*mlist):
        """
        TASK-4's task(Challenge-1)
        :param mlist: dynamic input of n lists
        :return: returns a single list with all the values present in each list given as input
        """
        logging.info("The given list for this operation is %s", mlist)
        result = list()
        for i in mlist:
            if(type(i)==list):
                result.extend(i)
        logging.info("The output of the operation is %s", result)
        return result

    def extract_dict_in_given_list(self, l):
        """
        TASK-3's task
        Try to extract only a dict collection form list l
        :param l: input list
        :return: returning a list containing all the dicts present in the given list
        """
        try:
            l1 = []
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if (type(i) == dict):
                    l1.append(i)
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def extract_tuple_in_given_list(self, l):
        """
        TASK-3's task
        Try to extract only a tuple collection form list l
        :param l: input list
        :return: returning a list containing all the tuples present in the given list
        """
        try:
            l1 = []
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if (type(i) == tuple):
                    l1.append(i)
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_alnum_in_given_list(self, l):
        """
        TASK-3's task
        Try to extract only alnum strings form list l
        :param l: input list
        :return: returning a list containing all the alnums present in the given list
        """
        try:
            l1 = []
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if (type(i) == list or type(i) == tuple or type(i) == set):
                    for j in i:
                        if (type(j) == str and j.isalnum()):
                            l1.append(j)
                if (type(i) == dict):
                    for k, v in i.items():
                        if (type(k) == str and k.isalnum()):
                            l1.append(k)
                        if (type(v) == str and v.isalnum()):
                            l1.append(v)
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def unwrap_all_collections_to_list(self, l):
        """
        TASK-3's task
        unwrap all collections to list
        :param l: input list
        :return: returning a list containing all the collections present in the given list
        """
        try:
            l1 = []
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if (type(i) == list or type(i) == tuple or type(i) == set):
                    for j in i:
                        l1.append(j)
                elif (type(i) == dict):
                    for k, v in i.items():
                        l1.append(k)
                        l1.append(v)
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
