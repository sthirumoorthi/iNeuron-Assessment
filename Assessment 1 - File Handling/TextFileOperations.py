import logging
logging.basicConfig(filename="FileOpLog.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class ReadText():
    """
    Class to read the text file and replace the content with the supplied string.

    __init__: This default method will create a new file with the supplied content. 
                Class object should have 2 parameters (File name and File content)

    readFile: This user defined method will read the file and return the data as string.
    updateFile: This user defined method will read the file content in "r+" mode and replce the specific string 
                using replace method. The replaced content will be updated in the file itself.
    """


    def __init__(self, filename, init_content):
        """
        This default method will create the file with the specified file content during the object initialization.
        """
        logging.info("... New object was initiated ...")
        self.filename = filename
        self.init_content = init_content
        try:
            with open(self.filename, "w") as file:
                file.write(self.init_content)
        except Exception as err:
            logging.exception(f"Exception occurred during object initiation. Error: {err}")

    def readFile(self):
        """
        This method will open the file in read mode and return the file contents/data as a string
        """
        try:
            logging.info(f"File read operation executed for file: {self.filename}")
            with open(self.filename, "r") as file:
                data = file.read()
        except Exception as err:
            logging.exception(f"Exception occurred while reading the file. Error: {err}")

        return data

    def updateFile(self, old_str, new_str):
        """
        This method will open the file in "r+" mode and replace the specified string using replace() method.
        New or replaced string will then be updated in the original file.
        """
        try:
            logging.info(f"File update operation executed for the file: {self.filename}")
            with open(self.filename, "r+") as file:
                data = file.read()
                new_data = data.replace(old_str, new_str)
                file.seek(0)
                file.write(new_data)
        except Exception as err:
            logging.exception(f"Exception occurred while replacing file content/updating the file. Error: {err}")



# Main stream
if __name__ == '__main__':
    logging.info("*** Application started ***")
    file1 = ReadText("TextFile.txt", "This is a placement assignment")
    print("Before replace:", file1.readFile())
    file1.updateFile("placement", "screening")
    print("After replacing:", file1.readFile())
    logging.info("*** End of Application process ***")