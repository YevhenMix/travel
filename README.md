<h1> Сайт по поиску маршрута по заданным параметрам. </h1>
<h2>Задание:</h2>
Поиск маршрута перемещения из одной точки в другую. Задача делится на 3 части - населенные пункты, поезда, маршруты.

<h2>Населенные пункты.</h2>
Реализовать добавление, редактирование, удаление населенного пункта, а также постраничный просмотр всех доступных населенных пунктов. У населенного пункта есть лишь название

<h2>Поезда.</h2>
Реализовать добавление, редактирование, удаление поезда, а также постраничный просмотр всех доступных поездов. У поезда есть уникальный код (название), начало маршрута, конец маршрута и время в пути в условных единицах. Из одной точки в другую может быть несколько поездов, но они должны отличаться по времени в пути.

<h2>Маршруты.</h2>
Пользователь выбирает начальный и конечный пункт маршрута, а также указывает максимальное время в пути. Также пользователь может добавить сколь угодно промежуточных городов, через которые должен пролегать маршрут. Ему загружаются подходящие под условия маршруты. Возле каждого маршрута должна быть кнопка, позволяющая сохранить данный маршрут, задав ему имя. При поиске маршрутов, необходимо обращать внимание на направление движения поезда.

<h2>Вывод результатов.</h2>
Вывод маршрутов сортируется по наименьшему времени в пути. Т.е. первым отображается маршрут, с наименьшим временем в пути. Описание маршрута должно содержать информацию о том, откуда и куда ведет этот маршрут, время в пути, а также содержать список всех поездов, которые есть в этом маршруте с указанием номера поезда, откуда\куда и времени в пути.
В случае, если маршрут не найден, вывести сообщение - "Маршрута удовлетворяющего условиям поиска не существует " Если же, заданное время в пути меньше, чем минимальное время маршрута, тогда сообщение "Время в дороге больше выбранного Вами. Измените время."

<h2>Сохраненные маршруты.</h2>
Должна быть отдельная страница с просмотром маршрутов. Маршрут можно только сохранить, посмотреть и удалить. Редактировать сохраненный маршрут нельзя.

<h2>Доступ к сайту.</h2>
Доступ к добавлению\редактированию Поездов\Городов, а также удалению любых записей, должен быть только у зарегистрированных пользователей.
