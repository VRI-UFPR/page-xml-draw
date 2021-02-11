gen-page: assets/schema/pagecontent.xsd page_xml_draw/gends/user_methods.py
	generateDS \
	-o page_xml_draw/gends/page.py \
	--user-method=$(word 2, $^) \
	$(word 1, $^)
