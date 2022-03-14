fetch('/list_itens')
      .then(function (response) {
          return response.json();
      }).then(function (text) {
          console.log('GET response:');
          console.log(text.greeting); 
      });