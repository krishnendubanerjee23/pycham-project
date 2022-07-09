import logging

logging.basicConfig(filename='ds_class.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


class stringClass:

    def __init__(self, ip_str):
        logging.info('string Constructor is called....')
        self.ip_str = ip_str

    def extractStrInRange(self):
        try:
            logging.info('extracting data from index one to index 300 with a jump of 3')
            return self.ip_str[0:300:3]
        except Exception as e:
            logging.error(e)

    def reverseStr(self):
        try:
            logging.info('reversing a string without using reverse function')
            return self.ip_str[::-1]
        except Exception as e:
            logging.error(e)

    def splitStrAfterUpper(self):
        try:
            logging.info('spliting a string after conversion of entire string in uppercase')
            return self.ip_str.upper().split(' ')
        except Exception as e:
            logging.error(e)

    def strToLower(self):
        try:
            logging.info('converting the whole string into lower case')
            return self.ip_str.lower()
        except Exception as e:
            logging.error(e)

    def strCapitilize(self):
        try:
            logging.info('capitalizing the whole string')
            return self.ip_str.capitalize()
        except Exception as e:
            logging.error(e)

    def checkAlphaNum(self, str):
        try:
            logging.info('checking alpha numeric in string')
            return str.isalnum()
        except Exception as e:
            logging.error(e)

    def checkAlpha(self, str):
        try:
            logging.info('checking alphabet in string')
            return str.isalpha()
        except Exception as e:
            logging.error(e)

    def expandTabStr(self, str):
        try:
            logging.info('expand tab is performing on a string')
            return str.expandtabs()
        except Exception as e:
            logging.error(e)

    def trim(self, str):
        try:
            logging.info('removing space around str')
            return str.strip()
        except Exception as e:
            logging.error(e)

    def ltrim(self, str):
        try:
            logging.info('removing space left of str')
            return str.lstrip()
        except Exception as e:
            logging.error(e)

    def rtrim(self, str):
        try:
            logging.info('removing space right of str')
            return str.rstrip()
        except Exception as e:
            logging.error(e)

    def replaceStr(self, word, str1, str2):
        try:
            logging.info('Replacing a string character by another character')
            return word.replace(str1, str2)
        except Exception as e:
            logging.error(e)

    def centerStr(self, str):
        try:
            logging.info('performing string center function')
            return str.center(20, '*')
        except Exception as e:
            logging.error(e)


class listClass:

    def __init__(self, ls1, ls2):
        logging.info('list Constructor is called....')
        self.ls1 = ls1
        self.ls2 = ls2

    def extractAllListEntity(self):
        try:
            logging.info('extracting all list entity from the collection')
            for i in self.ls1:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def filterOddFromList(self):
        try:
            logging.info('Try to filter out all the odd values out all numeric data which is a part of a list')
            for i in self.ls1:
                if type(i) == list:
                    for k in i:
                        if type(k) == int:
                            if k % 2 != 0:
                                logging.info(k)
        except Exception as e:
            logging.error(e)

    def reverseAList(self):
        try:
            logging.info('Reversing List without for loop')
            return self.ls2[::-1]
        except Exception as e:
            logging.error(e)

    def access234FromList(self):
        try:
            logging.info('Accessing 234 from List without for loop')
            return self.ls2[7][0]
        except Exception as e:
            logging.error(e)

    def access456FromList(self):
        try:
            logging.info('Accessing 456 from List without for loop')
            return self.ls2[5][1]
        except Exception as e:
            logging.error(e)

    def extractOnlyList(self):
        try:
            logging.info('extract List 1 from the collection without for loop')
            logging.info(self.ls2[5])
            logging.info('extract List 2 from the collection without for loop')
            logging.info(self.ls2[6])
            logging.info('extract List 3 from the collection without for loop')
            logging.info(self.ls2[8][234])
        except Exception as e:
            logging.error(e)


class tupleClass:

    def __init__(self,ls):
        logging.info('tuple Constructor is called....')
        self.ls=ls

    def extractTuples(self):
        try:
            logging.info('extracting all tuple entity from the collection')
            for i in self.ls:
                if type(i) == tuple:
                    logging.info(i)
        except Exception as e:
            logging.error(e)


class dictClass:

    def __init__(self,ls1,ls2):
        logging.info('dict Constructor is called....')
        self.ls1=ls1
        self.ls2=ls2

    def extractDictEntity(self):
        try:
            logging.info('extracting all dict entity from the collection')
            for i in self.ls1:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def noOfKeysDict(self):
        try:
            logging.info('dict key count function was initiated')
            keyCount = 0

            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        keyCount += 1

            return keyCount
        except Exception as e:
            logging.error(e)


    def extractSudh(self):
        try:
            logging.info('extracting sudh from the collection without for loop')
            return self.ls2[8]['key1']
        except Exception as e:
            logging.error(e)

    def extractValueFromDict(self):
        try:
            logging.info('extracting all the dict values from the collection')
            logging.info('extracting first value without for loop')
            logging.info(self.ls2[8]['key1'])
            logging.info('extracting second value without for loop')
            logging.info(self.ls2[8][234])
        except Exception as e:
            logging.error(e)


class setClass:

    def __init__(self,ls):
        logging.info('set Constructor is called....')
        self.ls=ls

    def lsToSet(self):
        try:
            logging.info('conversion of list into set')
            return set(self.ls)
        except Exception as e:
            logging.error(e)

class genericClass:

    def __init__(self, ls1):
        logging.info('generic Constructor is called....')
        self.ls1 = ls1


    def extractNumericFromCollection(self):
        try:
            logging.info('extracting only numeric value from the collection')
            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == int:
                            logging.info(j)
                        if type(i[j]) == int:
                            logging.info(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int:
                            logging.info(k)
                elif type(i) == int:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def sumOfNumericFromCollection(self):
        try:
            logging.info('sum of numeric value from the collection')
            s1 = 0
            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == int:
                            s1 = s1 + j
                        if type(i[j]) == int:
                            s1 = s1 + i[j]
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int:
                            s1 = s1 + k
                elif type(i) == int:
                    s1 = s1 + i

            return s1
        except Exception as e:
            logging.error(e)

    def extractINeuron(self):
        try:
            logging.info('Extract ineuron from the collection')
            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == str:
                            if j == 'ineuron':
                                logging.info(j)
                        if type(i[j]) == str:
                            if i[j] == 'ineuron':
                                logging.info(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == str:
                            if k == 'ineuron':
                                logging.info(k)
                elif type(i) == str:
                    if i == 'ineuron':
                        logging.info(i)
        except Exception as e:
            logging.error(e)

    def numberOfOccurenceFromCollection(self):
        try:
            logging.info('number of occurences of all the data from the collection')
            l1 = []

            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                        if type(i[j]) == int or type(i[j]) == str:
                            l1.append(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int or type(k) == str:
                            l1.append(k)
                elif type(i) == int or type(i) == str:
                    l1.append(i)

            for i in set(l1):
                logging.info('{0}:{1}'.format(i, l1.count(i)))
        except Exception as e:
            logging.error(e)

    def extractAlphaNumFromCollection(self):
        try:
            logging.info('extracting alphanumeric data from the collection')
            l1 = []

            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == str:
                            if j.isalnum():
                                l1.append(j)
                        if type(i[j]) == str:
                            if i[j].isalnum():
                                l1.append(i[j])
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == str:
                            if k.isalnum():
                                l1.append(k)
                elif type(i) == str:
                    if i.isalnum():
                        l1.append(i)

            return l1
        except Exception as e:
            logging.error(e)

    def multiplicationOfNumFromCollection(self):
        try:
            logging.info('multiplication of numeric value from the collection')
            s1 = 1
            for i in self.ls1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == int:
                            s1 = s1 * j
                        if type(i[j]) == int:
                            s1 = s1 * i[j]
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for k in i:
                        if type(k) == int:
                            s1 = s1 * k
                elif type(i) == int:
                    s1 = s1 * i

            return s1
        except Exception as e:
            logging.error(e)


# creating StringClass object and passing string data to constructor
stringObj = stringClass("this is My First Python programming class and i am learNING python string and its function")

logging.info('------------------------------------------stringClass object got created------------------------------------------')

logging.info(stringObj.extractStrInRange())

logging.info(stringObj.reverseStr())

logging.info(stringObj.splitStrAfterUpper())

logging.info(stringObj.strToLower())

logging.info(stringObj.strCapitilize())

logging.info(stringObj.checkAlphaNum('123abc'))

logging.info(stringObj.checkAlpha('abcdef'))

logging.info(stringObj.expandTabStr('My Name is\t Udayavel\t RPA Developer'))

logging.info(stringObj.trim('  udaya  '))

logging.info(stringObj.ltrim('  udaya  '))

logging.info(stringObj.rtrim('  udaya  '))

logging.info(stringObj.replaceStr('udayavel', 'a', 'v'))

logging.info(stringObj.centerStr('udaya'))

logging.info('------------------------------------------stringClass completed------------------------------------------')

# creating listClass object and passing list data to constructor
listObj = listClass([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]],
                      [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}])

logging.info('------------------------------------------listClass object got created------------------------------------------')

listObj.extractAllListEntity()

listObj.filterOddFromList()

logging.info(listObj.reverseAList())

logging.info(listObj.access234FromList())

logging.info(listObj.access456FromList())

listObj.extractOnlyList()

logging.info('------------------------------------------listClass completed------------------------------------------')

# creating tupleClass object and passing tuple data to constructor
tupleObj = tupleClass([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])

logging.info('------------------------------------------tupleClass object got created------------------------------------------')

tupleObj.extractTuples()

logging.info('------------------------------------------tupleClass completed------------------------------------------')

# creating dictClass object and passing dict data to constructor
dictObj = dictClass([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]],
                      [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}])

logging.info('------------------------------------------dictClass object got created------------------------------------------')

dictObj.extractDictEntity()

logging.info(dictObj.noOfKeysDict())

logging.info(dictObj.extractSudh())

logging.info(dictObj.extractValueFromDict())

logging.info('------------------------------------------dictClass completed------------------------------------------')

# creating genericClass object and passing generic data to constructor
setObj = setClass([1,2,2,3,4,4,5,6,7,8,8,9,9])

logging.info('------------------------------------------setClass object got created------------------------------------------')

logging.info(setObj.lsToSet())

logging.info('------------------------------------------setClass completed------------------------------------------')

# creating genericClass object and passing generic data to constructor
genericObj = genericClass([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                       {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])

logging.info('------------------------------------------genericClass object got created------------------------------------------')

genericObj.extractNumericFromCollection()

logging.info(genericObj.sumOfNumericFromCollection())

genericObj.extractINeuron()

genericObj.numberOfOccurenceFromCollection()

logging.info(genericObj.extractAlphaNumFromCollection())

logging.info(genericObj.multiplicationOfNumFromCollection())

logging.info('------------------------------------------genericClass completed------------------------------------------')
