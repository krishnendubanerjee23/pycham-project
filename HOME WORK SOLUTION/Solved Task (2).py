import logging

logging.basicConfig(filename="stringTasks.log", level=logging.DEBUG)


class StringTasks:
    """
    This class is on different tasks on strings given by sudhanshu sir in five different tasks given till date.
    """

    def extract_data(self, s):
        """
        TASK-1's task
        1 . Try to extract data from index one to index 300 with a jump of 3
        :param s: input string
        :return: slices the string s with a step of 3 and starting point of 1, ending point of 300
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s1 = s[1:300:3]
            logging.info("The output of the operation is %s", s1)
            return s1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def reverse_given_string(self, s):
        """
        TASK-1's task
        2 . Try to reverse a string without using reverse function
        :param s: input string
        :return: reverses the given string
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s2 = s[::-1]
            logging.info("The output of the operation is %s", s2)
            return s2
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def split_uppercase_string(self, s):
        """
        TASK-1's task
        3. Try to split a string after conversion of entire string in uppercase
        :param s: input string
        :return: it returns a list of string. which were converted to uppercase and then splitted using split().
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s3 = s
            s4 = s3.upper().split(' ')
            logging.info("The output of the operation is %s", s4)
            return s4
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def conversion_to_lower_string(self,s):
        """
        TASK-1's task
        4. try to convert the whole string into lower case
        :param s: input string
        :return: return the given string with all characters in lowercase
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s5 = s
            s6 = s5.lower()
            logging.info("The output of the operation is %s", s6)
            return s6
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def conversion_to_capitalize_string(self,s):
        """
        TASK-1's task
        5 . Try to capitalize the whole string
        :param s: input string
        :return: return the given string in capitalize form
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s7 = s
            s8 = s7.capitalize()
            logging.info("The output of the operation is %s", s8)
            return s8
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def expandtab_the_given_string(self,s):
        """
        TASK-1's task
        7. Try to give an example of expand tab
        :param s: input string
        :return: returns the given string with tab spaces
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s9 = s
            s10 = s9.expandtabs()
            logging.info("The output of the operation is %s", s10)
            return s10
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def strip_the_given_string(self,s):
        """
        TASK-1's task
        8.(i) Give an example of strip
        :param s: input string
        :return: returns the given string with stripping the extra spaces present on its left and right side
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s11 = s
            s12 = s11.strip()
            logging.info("The output of the operation is %s", s12)
            return s12
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def lstrip_the_given_string(self,s):
        """
        TASK-1's task
        8.(i) Give an example of lstrip
        :param s: input string
        :return: returns the given string with stripping the extra spaces present on its left side
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s13 = s
            s14 = s13.lstrip()
            logging.info("The output of the operation is %s", s14)
            return s14
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def rstrip_the_given_string(self,s):
        """
        TASK-1's task
        8.(i) Give an example of rstrip
        :param s: input string
        :return: returns the given string with stripping the extra spaces present on its right side
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s15 = s
            s16 = s15.rstrip()
            logging.info("The output of the operation is %s", s16)
            return s16
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def replacing_a_part_in_given_string(self,s,pr,tr):
        """
        TASK-1's task
        9.  Replace a string charecter by another charector by taking your own example
        :param s: input string
        :param pr: the part we want to replace
        :param tr: with what we want to replace
        :return:
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s17 = s
            s18 = s17.replace(pr,tr)
            logging.info("The output of the operation is %s", s18)
            return s18
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def filling_spaces_with_characters_in_given_string(self,s):
        """
        TASK-1's task
        10 . Try  to give a defination of string center function with and exmple
        :param s: input string
        :return: returns a strings with a fixed length and fills the characters if exists in header or trailer parts of string
        keeping the string at the center.
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s19 = s
            s20 = s19.center(20,'*')
            logging.info("The output of the operation is %s", s20)
            return s20
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

