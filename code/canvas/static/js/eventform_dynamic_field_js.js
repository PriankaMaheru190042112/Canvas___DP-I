// Add input field dynamically start

      $('.extra-fields-photo').click(function() {
        $('.new_photo').clone().appendTo('.photo_records_dynamic');
        $('.photo_records_dynamic .new_photo').addClass('single remove');
        $('.single .extra-fields-photo').remove();
        $('.single').append('<a href="#" class="remove-field btn-remove-photo">Remove Photo</a>');
        $('.photo_records_dynamic > .single').attr("class", "remove");
      
        $('.photo_records_dynamic input').each(function() {
          var count = 0;
          var fieldname = $(this).attr("name");
          $(this).attr('name', fieldname + count);
          count++;
        });
      
      });
      
      $(document).on('click', '.remove-field', function(e) {
        $(this).parent('.remove').remove();
        e.preventDefault();
      });


      // Add input field dynamically end