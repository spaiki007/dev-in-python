import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const domain = 'http://localhost:81';
//const domain = '';

export default new Vuex.Store({
  state: {
    domain,

    setting_editor: {

      language_url: domain + '/static/js/tinymce/lang/ru.js',
      language: 'ru',
      plugins: [
        'advlist autolink link lists charmap print preview hr anchor pagebreak spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime nonbreaking',
        'tinydrive save directionality emoticons paste image media imagetools',
      ],
      height: 400,
      toolbar: ['undo redo styleselect forecolor backcolor bolditalic underline bullist numlist outdent indent insertfile link image alignleft aligncenter alignright code'],
      tinydrive_token_provider: domain + '/jwt',
      tinydrive_upload_path: domain + '/tinymce/upload',

    },

  },

  mutations: {},
  actions: {},

});
