import validators
from nicegui import ui
from sqlalchemy import func
from starlette.responses import RedirectResponse

from db import ShortURL, Session
from styles import style
from util import create_short_url, get_host_url

ui.add_head_html(style)


@ui.page('/s/{short_key}')
def redirect_page(short_key: str):
    with Session() as session:
        short_url = session.query(ShortURL).filter_by(short_key=short_key).first()
        if short_url:
            short_url.visits += 1
            session.commit()
            return RedirectResponse(short_url.original_url)
        ui.notify('Invalid short URL', type='negative', position='top')
        return RedirectResponse('/')


with ui.column().classes('gradient-bg'):
    with ui.column().classes('main-container'):

        # Title row: icon + "ShortenX"
        with ui.row().classes('title-row'):
            ui.icon('link', size='3rem')
            with ui.column().classes('items-start'):
                ui.label('ShortenX').classes('text-3xl font-bold')
                ui.label('Modern URL Shortener').classes('text-sm opacity-90')

        # URL Shortening Card
        with ui.card().classes('glass-card hover-scale'):
            url_input = ui.input('Enter URL').props('outlined rounded autofocus clearable') \
                .classes('animated-input w-full mb-3')

            with ui.row().classes('w-full justify-center gap-2'):
                shorten_btn = ui.button('Shorten URL', on_click=lambda: process_url()) \
                    .props('icon=send rounded').classes('primary-button px-5 py-2')
                ui.button('Clear', on_click=lambda: url_input.set_value('')) \
                    .props('icon=delete rounded').classes('secondary-button px-5 py-2')

            # Result block as glass card to ensure consistent background color
            result_card = ui.card().classes('glass-card result-card hidden mt-3')
            with result_card:
                ui.label('Shortened URL:').classes('label-shortened-url')
                # Layout row: link on left, buttons on right
                with ui.element('div').classes('short-url-row'):
                    result_link = ui.link('', target='_blank').classes('result-link break-all')
                    with ui.element('div').classes('short-url-buttons'):
                        ui.button('Copy', on_click=lambda: ui.run_javascript(
                            f'navigator.clipboard.writeText(`{result_link.text}`)')) \
                            .props('icon=content_copy rounded').classes('primary-button')
                        ui.button('Test', on_click=lambda: ui.run_javascript(
                            f'window.open(`{result_link.text}`, "_blank")')) \
                            .props('icon=launch rounded').classes('secondary-button')

            progress = ui.linear_progress(0).classes('w-full mt-3 opacity-0')

        # Statistics Card
        with ui.card().classes('glass-card hover-scale'):
            ui.label('Statistics').classes('stats-title')
            with ui.row().classes('stats-grid'):
                with ui.column().classes('items-center'):
                    total_links = ui.label('0').classes('stats-number')
                    ui.label('Total Links').classes('stats-label')
                with ui.column().classes('items-center'):
                    total_visits = ui.label('0').classes('stats-number')
                    ui.label('Total Visits').classes('stats-label')


            async def update_stats():
                try:
                    with Session() as session:
                        total_links.text = str(session.query(func.count(ShortURL.id)).scalar() or 0)
                        total_visits.text = str(session.query(func.sum(ShortURL.visits)).scalar() or 0)
                except Exception as e:
                    ui.notify(f'Error updating stats: {str(e)}', type='negative', position='top')


            ui.timer(2.0, update_stats)


def process_url():
    url = url_input.value.strip()
    if not validators.url(url):
        ui.notify('Please enter a valid URL', type='negative', position='top')
        return

    # Show progress bar halfway
    progress.classes(remove='opacity-0')
    shorten_btn.disable()
    progress.value = 0.5

    try:
        short_key = create_short_url(url)
        short_url = f"{get_host_url()}/s/{short_key}"
        result_link.text = short_url
        result_link._props['href'] = short_url

        # Reveal the result block
        result_card.classes(remove='hidden', add='visible')
        ui.notify('URL shortened successfully!', type='positive', position='top')
    except Exception as e:
        ui.notify(f'Error: {str(e)}', type='negative', position='top')
    finally:
        # Hide progress bar
        progress.classes(add='opacity-0')
        progress.value = 0
        shorten_btn.enable()


if __name__ == '__main__':
    ui.run(title='ShortenX', reload=False, dark=False)
