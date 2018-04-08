function get_fibo(){
  var x = $("#id_number").val();
    $.ajax({  
          type: "GET",
          url: GET_FIBO,
          data: {"number": x},
          dataType: "json",
          // beforeSend: function(){$(".loader").show()},
          success: function(res) {
            console.log(res)
            $('#res-div').text(res.data.key + 'th fibbonacci number is: ' + res.data.value);
            $('#time-div').text('Total time taken: ' + res.time + ' miliseconds');
          },
          error: function(res){
            console.log(res);
          }
    });
}
