from django.template import Library
from django.utils.html import mark_safe
from django.views.decorators.csrf import csrf_protect, csrf_exempt



register = Library()

@csrf_protect
@register.filter
def comments_filter(comments_list):
    res = """
             <ul style="list-style-type:none;">
                <div class="col-md-12 mt-2">
                    {}
                </div> 
             </ul>
             """
    new_res = ''
    # print(comments_list)
    for comment in comments_list:
        
        new_res += """
                  <li>
                      <div class="col-md-12 mb-2 mt-2 p-0">
                          <small>{author}</small> | опубликовано: {timestamp}
                          <hr>
                          <p>{comment_text} | id={id}</p>
                          <button href="#" class="reply btn btn-link" data-id="{id}" data-parent={parent_id}>Ответить</button>
                          <form method="POST" class="comment-form form-group" id="form-{id} ">  
                              <textarea type="text" class="form-control" name="comment-text"></textarea><br>
                              <input type="submit" class="btn btn-primary submit-reply" data-id="{id}" data-submit-reply="{parent_id}" value="Отправить"></input>
                          </form>
                      </div> 
                  </li>
             """.format(id=comment['id'], author=comment['author'], timestamp=comment['timestamp'], comment_text=comment['comment_text'], parent_id=comment['parent_id']) # Получаем ID комментария
        if comment.get('children'): # ывп
             new_res += comments_filter(comment['children'])
    return mark_safe(res.format(new_res))