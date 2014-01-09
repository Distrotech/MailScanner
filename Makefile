all:

clean:

distclean:

install:
	install -d $(DESTDIR)/opt/MailScanner
	rsync -a dist/ $(DESTDIR)/opt/MailScanner/
