def process_begin_string(num1, num2):
    print("Hi from process_begin_string with %d %d" % (num1, num2))

def process_body_length(num1, num2):
    print("Hi from process_body_length with %d %d" % (num1, num2))

my_lookup_dict = {
	"8" : process_begin_string,
	"35": process_body_length
}

# Client
token = input("Enter a token: ")
if token in my_lookup_dict:
    my_lookup_dict[token](42, 52)
else:
    print("No handler function for token: %s" % token)
