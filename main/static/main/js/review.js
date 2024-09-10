async function getform(){
  let promise=await fetch("/addreview")
  if (promise.ok)
  {
    let html=await promise.text()
    let formdiv = document.querySelector(".formcontent")
    formdiv.innerHTML=html
  }
}
getform()
