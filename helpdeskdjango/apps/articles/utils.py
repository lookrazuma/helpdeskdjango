from .models import Comment


def get_children(qs_children): # функция принимает в себя queryset, ищет дочерние комментарии
    result =[]
    for comment in qs_children:
        comm = {
            'id': comment.id,
            'comment_text': comment.comment_text,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d %h:%m'),
            'author': comment.user,
            'is_child': comment.is_child,
            'parent_id': comment.get_parent
        }
        if comment.comment_children.exists(): # Проверяем через exist есть ли у комментария дочерние комментарии
            # Если есть, создаём ключ children и записываем результат работы функции
            comm['children'] = get_children(comment.comment_children.all())
        result.append(comm)
    return result


def create_comments_tree(qs): 
    result = []
   
    for comment in qs: # Итерируемся по QuerySet
        
        comm = {
            'id': comment.id,
            'comment_text': comment.comment_text,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d %h:%m'),
            'author': comment.user,
            'is_child': comment.is_child,
            'parent_id': comment.get_parent
        }

        if comment.comment_children:
            comm['children'] = get_children(comment.comment_children.all())
        if not comment.is_child:
            result.append(comm)
    
    return result