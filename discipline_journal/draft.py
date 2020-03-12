        widgets = {
        'date': forms.DateTimeInput(attrs={'class': 'datepicker'}),
    }

        <script>
      $(function () {
          $('.datepicker').datepicker({
              format:'YYYY-MM-DD',
              locale: 'ru',
          });


      });