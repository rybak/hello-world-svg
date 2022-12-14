
all: output.svg output-bg.svg generated.html

output.svg: begin.svg generated.svg end.svg
	cat $^ >$@

output-bg.svg: begin.svg background.svg generated.svg end.svg
	cat $^ >$@

generated.svg: generate.py
	./generate.py >$@

generated.html: output.svg
	echo '<html><body style="background: #000;">' >$@
	cat $^ >>$@
	echo '</body></html>' >>$@

clean:
	rm -rf output.svg output-bg.svg generated.svg generated.html
