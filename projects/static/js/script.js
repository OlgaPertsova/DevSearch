let searchForms = document.getElementById('search');
  let pageLinks = document.querySelectorAll('.page-link');

  if(searchForms){
    for(let i=0; pageLinks.length > i; i++){
      pageLinks[i].addEventListener('click', function(e){
        e.preventDefault();

        let page = this.dataset.page;
        searchForms.innerHTML += `<input value=${page} name="page" type="hidden">`;

        searchForms.submit();
      })
    }
  }
