/*------------------------ vars ------------------------*/
var file = "https://rmorfin.heyuhnem.com/sitemap.xml";


/*------------------------ parser ------------------------*/
var Connect = new XMLHttpRequest();
Connect.open("GET", file , false);
Connect.setRequestHeader("Content-Type", "text/xml");
Connect.send(null);
var TheDocument = Connect.responseXML;
var XMLs = TheDocument.childNodes[0];


/*------------------------ output ------------------------*/
document.write("<table>");
document.write("<tr><th>TITLE</th><th>ARTIST</th><th>COUNTRY</th><th>COMPANY</th><th>PRICE</th><th>YEAR</th></tr>");
for (var i = 0; i < XMLs.children.length; i++){
    var XML = XMLs.children[i];

    var TITLE = XML.getElementsByTagName("TITLE");
    var ARTIST = XML.getElementsByTagName("ARTIST");
    var COUNTRY = XML.getElementsByTagName("COUNTRY");
    var COMPANY = XML.getElementsByTagName("COMPANY");
    var PRICE = XML.getElementsByTagName("PRICE");
    var YEAR = XML.getElementsByTagName("YEAR");

    document.write("<tr><td>");
    document.write(TITLE[0].textContent.toString());
    document.write("</td><td>");
    document.write(ARTIST[0].textContent.toString());
    document.write("</td><td>");
    document.write(COUNTRY[0].textContent.toString());
    document.write("</td><td>");
    document.write(COMPANY[0].textContent.toString());
    document.write("</td><td>");
    document.write(PRICE[0].textContent.toString());
    document.write("</td><td>");
    document.write(YEAR[0].textContent.toString());
    document.write("</td></tr>");

}//for

document.write("</table>");
