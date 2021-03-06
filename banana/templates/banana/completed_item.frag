{% load imagetags %}
<div class="completed-item-view update-view {% if completed_item.promoted %}promoted{% endif %}">
	{% if show_completed_item_user %}
		{% if completed_item.user.get_profile.photo %}
			<a href="{{ completed_item.user.get_absolute_url }}"><img class="person-photo" src="{{ completed_item.user.get_profile.photo.image.url|fit_image:"50x50" }}" title="{{ completed_item.user.get_full_name}}" alt="{{ completed_item.user.get_full_name}}" /></a>
		{% else %}
			<a href="{{ completed_item.user.get_absolute_url }}"><img class="person-photo" src="{{STATIC_URL}}person/BlankIcon150x150.jpg" width="50" height="50" /></a>
		{% endif %}
		<a href="{{ completed_item.user.get_absolute_url }}">{{ completed_item.user.get_full_name }}</a>
	{% endif %}

	<div class='rendered'>
		{{ completed_item.rendered|safe }}
	</div>

	{% if not hide_meta %}
		<div class="update-meta">
			{% if completed_item.link %}
				<a class='promoted-link' href="{{ completed_item.link}}">
					<i class='icon-external-link'></i>
				</a>
			{% endif %}
			<div class="update-timestamp">
				<a href="{{ completed_item.get_absolute_url }}">
					{{ completed_item.created|timesince }} ago
				</a>
			</div>
		</div>
	{% endif %}
	{% if not hide_rocks %}
		{% if completed_item.user == request.user or request.user in completed_item.rock_users or not request.user.is_authenticated %}
			{% if completed_item.rock_count %}
				<div class="completed-item-rock">
					Rocked!
					{% if completed_item.rock_count %}({{ completed_item.rock_count}}){% endif %}
				</div>
			{% endif %}
		{% else %}
			<div class="completed-item-rock">
				<a href="." onclick="rockCompletedItem('{{ completed_item.get_api_url }}', {{ completed_item.rock_count}}, $(this).parent()); return false;">
					Rock! {% if completed_item.rock_count %}({{ completed_item.rock_count}}){% endif %}
				</a>
				
			</div>
		{% endif %}
	{% endif %}

</div> <!--/completed-item-->

