/*

urls = [
  "https://httpstatuses.com/200",
  "https://httpstatuses.com/200",
  "https://httpstatuses.com/503"
]

var text = "\n"
var icon = ""
  
async function getStatus(arr){
  
  let urlset = arr;
  
  for (item in urlset) {
    try {

    // makes page request and gets status

    var req = new Request(urlset[item])
    var body = await req.loadString()
    var res = req.response
    var status = res.statusCode

    // removes unnecessary http text from output
    var urlString = urlset[item].replace(/(^\w+:|^)\/\//,'');

    // output for success   
    text += status.toString() + " " + urlString + "\n"

    } catch(err) {

    // output for failure
    text += status.toString() + " " + urlString + "\n"
    }
  }
  console.log(text);
}

getStatus(urls);

*/