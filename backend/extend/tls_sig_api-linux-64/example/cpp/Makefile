CPP = g++
ARCH=$(shell getconf LONG_BIT)
CFLAGS= -g -I../../include -I../../include/tls_sig_api -Wall -fPIC
LIBS= -L../../linux/$(ARCH)/lib/jsoncpp ../../openssl-dynamic/lib/libcrypto.a -ljsoncpp -ldl -lz

all: tls_licence_tools

tls_licence_tools: tls_licence_tools.o ../../src/libtlsignature.a
	$(CPP) $^ -Wall -o $@ $(CFLAGS) $(LIBS)

.cpp.o:
	$(CPP) $(CFLAGS) -c $*.cpp

clean:  
	-rm -f *.o *.a tls_licence_tools TAGS

.PHONY: all clean
