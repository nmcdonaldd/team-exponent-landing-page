function hideToggle(id) {
      var x = document.getElementById(id);
      if (x.style.visibility == 'hidden') {
          x.style.visibility = 'visible';
      } else if (x.style.visibility == 'visible') {
          x.style.visibility = 'hidden';
      } else {
        x.style.visibility = 'visible';
      }
  }
