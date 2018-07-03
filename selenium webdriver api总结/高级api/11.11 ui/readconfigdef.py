def read_ini_file(ini_file_path,section_name,option_name):
    cf = ConfigParser.ConfigParser()
    cf.read(ini_file_path)
    try:
        value = cf.get(section_name,option_name)
    except:
        print "the specific seciton or the specific option doesn't exit!"
        return None
    else:
        return value


print read_ini_file(os.path.dirname(os.path.abspath(__file__)) + "\db.ini","gloryroad","username")
