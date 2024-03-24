import ipaddress as ip

class Validation:
    def __init__ (self):
        pass
    
    def validIp(self, ip_string:str): 
        try:
            ip_object = ip.ip_address(ip_string)#if the string is a valid IPv4 or IPv6 address, a new IP address object will be created
            return True
        except ValueError:#if the string is not a valid IP address, a value error will be raised
            return False

    def validPort(self, port:str):
        try:
            if 1 <= int(port) <= 65535:#a port number can be any integer between 1 and 65535 inclusive
                return True
            else:
                raise ValueError #if the integer does not fit into the parameters (i.e. it is not a valid port number), a value error will be raised
        except ValueError:#any non-integer inputs or incorrect port numbers (see above) will raise a value error
            if len(port) == 0:#this checks if the length is 0 i.e. if nothing was entered
                return True
            else:
                return False
            
