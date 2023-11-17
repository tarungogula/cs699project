document.addEventListener('DOMContentLoaded', function() {
    const formset = document.getElementById('id_videos-TOTAL_FORMS');
    const addVideoButton = document.getElementById('add-video');
    const videoFormset = document.getElementById('video-formset');
    
    // Access the data attribute
    let formCount = parseInt(videoFormset.dataset.totalForms, 10);
    
    addVideoButton.addEventListener('click', function() {
      const newForm = videoFormset.firstElementChild.cloneNode(true);
      const newFormId = `id_videos-${formCount}-`;
      newForm.querySelectorAll('[id^="id_videos-0-"]').forEach(el => {
        el.id = el.id.replace('id_videos-0-', newFormId);
        el.name = el.name.replace('videos-0-', `videos-${formCount}-`);
        el.value = '';
      });
      
      // Ensure the cloned form has a unique ID
      newForm.id = `form-${formCount}`;
      
      videoFormset.appendChild(newForm);
      formCount += 1;
      formset.value = formCount;
    });
  });
  