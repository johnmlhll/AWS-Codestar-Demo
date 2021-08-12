/**
 * Function 1 - changeFont() - changes font for better accessibility
 */

 function changeFont() {
    if(this.document.getElementById("main_content").style.fontSize === '1.2em') {
      document.getElementById("main_content").style.fontSize = '1.5em';
      document.getElementsByClassName("buttons").style.fontSize = '1.3em';
    } else {
      document.getElementById("main_content").style.fontSize = '1.2em';
      document.getElementsByClassName("buttons").style.fontSize  = '0.9em';
    }
  }