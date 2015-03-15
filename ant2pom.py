from xml.dom import minidom
file = open("F:\\nuevoPomBatchSpring.xml",'w')
xmldoc = minidom.parse('F:\\wks\\buildBatch.xml')
itemlist = xmldoc.getElementsByTagName('jar')
for s in itemlist:
    value = s.attributes['jarfile'].value
    jar = value.replace('${dist}/lib/','')
    includes = s.attributes['includes'].value.split(",")
    file.write("<execution>")
    file.write("\t<id>"+jar+"</id>")
    file.write("\t<goals>")
    file.write("\t\t<goal>jar</goal>")
    file.write("\t</goals>")
    file.write("\t<phase>package</phase>")
    file.write("\t<configuration>")
    file.write("\t\t<finalName>"+jar.replace('.jar','')+"</finalName>")
    file.write("\t\t<includes>")
    for inc in includes:
        file.write("\t\t\t<include>"+inc+"</include>")
    file.write("\t\t</includes>")
    file.write("\t</configuration>")
    file.write("</execution>")
file.close()
