#!/usr/bin/python

import time
import requests
from bs4 import BeautifulSoup

viewState = ''
eventValidation = ''
init_viewState = '/wEPDwUKMTg1NDM2OTM0NQ9kFgJmD2QWAgIDD2QWCgIBD2QWCAIBDw8WAh4LTmF2aWdhdGVVcmwFwAFodHRwczovL3d3dy5nb29nbGUuY29tL2EvY21zLmJhLmdvdi5ici9TZXJ2aWNlTG9naW4/c2VydmljZT1tYWlsJnBhc3NpdmU9dHJ1ZSZybT1mYWxzZSZjb250aW51ZT1odHRwJTNBJTJGJTJGbWFpbC5nb29nbGUuY29tJTJGYSUyRmNtcy5iYS5nb3YuYnIlMkYmYnN2PTFlaWM2eXU5b2E0eTMmbHRtcGw9ZGVmYXVsdCZsdG1wbGNhY2hlPTJkZAIDDw8WAh8ABSdodHRwOi8vd3d3LnlvdXR1YmUuY29tL2NhbWFyYWRlc2FsdmFkb3JkZAIFDw8WAh8ABSFodHRwOi8vdHdpdHRlci5jb20vY2FtYXJhc2FsdmFkb3JkZAIHDw8WAh8ABShodHRwOi8vd3d3LmZhY2Vib29rLmNvbS9jYW1hcmFkZXNhbHZhZG9yZGQCAw9kFgQCBw9kFgJmD2QWCgIBDxAPFgYeDURhdGFUZXh0RmllbGQFBm5vbWVfcB4ORGF0YVZhbHVlRmllbGQFAmlkHgtfIURhdGFCb3VuZGdkDxYxAgECAgIDAgQCBQIGAgcCCAIJAgoCCwIMAg0CDgIPAhACEQISAhMCFAIVAhYCFwIYAhkCGgIbAhwCHQIeAh8CIAIhAiICIwIkAiUCJgInAigCKQIqAisCLAItAi4CLwIwAjEWMRAFBFZhZG8FAjgwZxAFC1V6aWVsIEJ1ZW5vBQMxMDZnEAUPVG9pbmhvIENhcm9saW5vBQI3OWcQBQ1UaWFnbyBDb3JyZWlhBQI3OGcQBQlUZW8gU2VubmEFAjk0ZxAFBlN1w61jYQUCNzdnEAUQU8OtbHZpbyBIdW1iZXJ0bwUCNzVnEAUFU2Fiw6EFAjUwZxAFD1JvZ8OpcmlhIFNhbnRvcwUDMTAyZxAFD1JpY2FyZG8gQWxtZWlkYQUDMTA0ZxAFH1Byb2N1cmFkb3JpYSBKdXLDrWRpY2EgLSBQcm9qdXIFAjU2ZxAFDFByZXNpZMOqbmNpYQUCNDRnEAUYUGF1bG8gTWFnYWxow6NlcyBKw7puaW9yBQIzMWcQBQ1QYXVsbyBDw6JtYXJhBQIyOWcQBRBPcmxhbmRvIFBhbGhpbmhhBQIyNmcQBRBPZGlvc3ZhbGRvIFZpZ2FzBQIyMmcQBQ1Nb2lzw6lzIFJvY2hhBQIxOWcQBRJNYXVyw61jaW8gVHJpbmRhZGUFAzEwMGcQBQ9NYXJ0YSBSb2RyaWd1ZXMFAjk5ZxAFD01hcmNlbGxlIE1vcmFlcwUCOThnEAULTHVpeiBDYXJsb3MFAjczZxAFD0xvcmVuYSBCcmFuZMOjbwUCOTdnEAUKTGVvIFByYXRlcwUCNzJnEAUKS2lraSBCaXNwbwUCNzBnEAUOSm9zw6kgVHJpbmRhZGUFAjY5ZxAFD0ouIENhcmxvcyBGaWxobwUCNjhnEAUNSXJldWRhIFNpbHZhIAUCOTVnEAUOSWdvciBLYW5uw6FyaW8FAjkzZxAFDUhpbHRvbiBDb2VsaG8FAjY3ZxAFEkhlbnJpcXVlIENhcmJhbGxhbAUBOWcQBQ9IZWxpbyBGZXJyZWlyYSAFAjkyZxAFDEZlbGlwZSBMdWNhcwUCOTFnEAUMRsOhYmlvIFNvdXphBQMxMDdnEAUNRXV2YWxkbyBKb3JnZQUCNjRnEAUNRWR2YWxkbyBCcml0bwUCNjNnEAUMRHVkYSBTYW5jaGVzBQI2MmcQBR1EaXJldG9yaWEgTGVnaXNsYXRpdmEgLSBEaXJlbAUCNTRnEAUdRGlyZXRvcmlhIEZpbmFuY2VpcmEgLSBEaXJmaW4FAjU1ZxAFIERpcmV0b3JpYSBBZG1pbmlzdHJhdGl2YSAtIERpcmFkBQI1M2cQBQtEYW5pZWwgUmlvcwUCOTBnEAUNQ29udHJvbGFkb3JpYQUCNTJnEAULQ2V6YXIgTGVpdGUFAjg5ZxAFEEPDoXRpYSBSb2RyaWd1ZXMFAjYwZxAFDENhcmxvcyBNdW5pegUCMTBnEAUEQmVjYQUCODJnEAUQQW5hIFJpdGEgVGF2YXJlcwUCNThnEAURQWxmcmVkbyBNYW5ndWVpcmEFATdnEAURQWxleGFuZHJlIEFsZWx1aWEFAzEwM2cQBQ5BbGFkaWxjZSBTb3V6YQUBMmdkZAIDDxAPFgYfAQUJZGVzY3JpY2FvHwIFAmlkHwNnZBAVAgVUb2RvcwdEacOhcmlhFQIBMAE0FCsDAmdnZGQCBQ8QDxYGHwEFA2Fubx8CBQNhbm8fA2dkDxYKAgECAgIDAgQCBQIGAgcCCAIJAgoWChAFBDIwMTgFBDIwMThnEAUEMjAxNwUEMjAxN2cQBQQyMDE2BQQyMDE2ZxAFBDIwMTUFBDIwMTVnEAUEMjAxNAUEMjAxNGcQBQQyMDEzBQQyMDEzZxAFBDIwMTIFBDIwMTJnEAUEMjAxMQUEMjAxMWcQBQQyMDEwBQQyMDEwZxAFBDIwMDkFBDIwMDlnZGQCDQ8UKwACDxYEHwNnHgtfIUl0ZW1Db3VudAKyAWRkFgJmD2QWCGYPZBYCZg8VCAoxNC8wNi8yMDE3B0Rpw6FyaWEKTGVvIFByYXRlcyFQcmVzaWRlbnRlOiBMZW9uYXJkbyBTaWx2YSBQcmF0ZXMJUiQgMzM2LDAwDEJyYXPDrWxpYS9ERhVSZXByZXNlbnRhciBhIEPDom1hcmGdAWp1bnRvIGFvIFNlbmFkbyBGZWRlcmFsLCBubyBxdWUgc2UgcmVmZXJlIGEgYXNzaW5hdHVyYSBkbyBQcm90b2NvbG8gZGUgSW50ZW7Dp8O1ZXMsIHBvciBtZWlvIGRvIEluc3RpdHV0byBMZWdpc2xhdGl2byBCcmFzaWxlaXJvLCBubyBkaWEgMTQgZGUganVuaG8gZGUgMjAxNy5kAgEPZBYCZg8VCAoxNC8wNi8yMDE3B0Rpw6FyaWEPTWFydGEgUm9kcmlndWVzL1ZlcmVhZG9yYTogTWFydGEgUm9kcmlndWVzIFNvdXNhIGRlIEJyaXRvIENvc3RhCVIkIDMzNiwwMAxCcmFzw61saWEvREYVUmVwcmVzZW50YXIgYSBDw6JtYXJhnQFqdW50byBhbyBTZW5hZG8gRmVkZXJhbCwgbm8gcXVlIHNlIHJlZmVyZSBhIGFzc2luYXR1cmEgZG8gUHJvdG9jb2xvIGRlIEludGVuw6fDtWVzLCBwb3IgbWVpbyBkbyBJbnN0aXR1dG8gTGVnaXNsYXRpdm8gQnJhc2lsZWlybywgbm8gZGlhIDE0IGRlIGp1bmhvIGRlIDIwMTcuZAICD2QWAmYPFQgKMTQvMDYvMjAxNwdEacOhcmlhDFByZXNpZMOqbmNpYTdBc3Npc3RlbnRlIGRhIFByZXNpZMOqbmNpYTogVml2YWxkbyBFdmFuZ2VsaXN0YSBSaWJlaXJvCVIkIDMzNiwwMAxCcmFzw61saWEvREYVUmVwcmVzZW50YXIgYSBDw6JtYXJhnQFqdW50byBhbyBTZW5hZG8gRmVkZXJhbCwgbm8gcXVlIHNlIHJlZmVyZSBhIGFzc2luYXR1cmEgZG8gUHJvdG9jb2xvIGRlIEludGVuw6fDtWVzLCBwb3IgbWVpbyBkbyBJbnN0aXR1dG8gTGVnaXNsYXRpdm8gQnJhc2lsZWlybywgbm8gZGlhIDE0IGRlIGp1bmhvIGRlIDIwMTcuZAIDD2QWAmYPFQgKMTQvMDYvMjAxNwdEacOhcmlhD1RvaW5obyBDYXJvbGlubyhWZXJlYWRvcjogQW50w7RuaW8gQ2Fyb2xpbm8gQXJhdWpvIEZpbGhvCVIkIDMzNiwwMAxCcmFzw61saWEvREYVUmVwcmVzZW50YXIgYSBDw6JtYXJhnQFqdW50byBhbyBTZW5hZG8gRmVkZXJhbCwgbm8gcXVlIHNlIHJlZmVyZSBhIGFzc2luYXR1cmEgZG8gUHJvdG9jb2xvIGRlIEludGVuw6fDtWVzLCBwb3IgbWVpbyBkbyBJbnN0aXR1dG8gTGVnaXNsYXRpdm8gQnJhc2lsZWlybywgbm8gZGlhIDE0IGRlIGp1bmhvIGRlIDIwMTcuZAIPDxQrAAJkEBYAFgAWAGQCCQ9kFgQCAQ8WAh8EAhMWJmYPZBYCZg8VAw9mcmVxdWVuY2lhLmFzcHgAGUZyZXF1w6puY2lhIGRlIFZlcmVhZG9yZXNkAgEPZBYCZg8VAwlhdGFzLmFzcHgAGUF0YXMgU2Vzc8O1ZXMgT3JkaW7DoXJpYXNkAgIPZBYCZg8VAy5odHRwOi8vMTc3LjEzNi4xMjMuMTQ5L2V4dC8/Z2V0PWNvbnRyYXRvc19tb2RzBl9ibGFuawlDb250cmF0b3NkAgMPZBYCZg8VAwxkZXNwZXNhLmFzcHgAD0Rlc3Blc2FzIFZpYWdlbWQCBA9kFgJmDxUDF3ZlcmVhZG9yZXNfc2Vzc29lcy5hc3B4ABdEaXNjdXJzb3MgZGUgVmVyZWFkb3Jlc2QCBQ9kFgJmDxUDEm1zZ19leGVjdXRpdm8uYXNweAAWTWVuc2FnZW5zIGRvIEV4ZWN1dGl2b2QCBg9kFgJmDxUDCnZldG9zLmFzcHgABVZldG9zZAIHD2QWAmYPFQMPb3JkZW1kb2RpYS5hc3B4AAxPcmRlbSBkbyBEaWFkAggPZBYCZg8VAw9vcmNhbWVudG8yLmFzcHgACk9yw6dhbWVudG9kAgkPZBYCZg8VAyVleGVjdWNhb19vcmNhbWVudGFyaWFfZmluYW5jZWlyYS5hc3B4ADdFeGVjLiBPcsOnYW1lbnTDoXJpYSBlIEZpbmFuY2VpcmEgLyBBY29tcGFuaGFtLiBEacOhcmlvZAIKD2QWAmYPFQMXcGFyZWNlcl9wcmV2aW9fdGNtLmFzcHgAFlBhcmVjZXIgUHLDqXZpbyBkbyBUQ01kAgsPZBYCZg8VAxlwcm9kdWNhb19sZWdpc2xhdGl2YS5hc3B4ACRSZXN1bW8gUHJvZHXDp8OjbyBMZWdpc2xhdGl2YSBBbnVhbCBkAgwPZBYCZg8VAxZwcmVzdGFjYW9fY29udGFzMi5hc3B4ABVQcmVzdGHDp8OjbyBkZSBDb250YXNkAg0PZBYCZg8VAy5odHRwOi8vMTc3LjEzNi4xMjMuMTQ5L2V4dC8/Z2V0PWxpY2l0YWNhb19tb2RzBl9ibGFuaxdQcm9jZXNzb3MgTGljaXRhdMOzcmlvc2QCDg9kFgJmDxUDRGh0dHA6Ly8xNzcuMTM2LjEyMy4xNTcvTGVnaXNsYXRpdm9EaWdpdGFsX2Fjb21wYW5oYW1lbnRvX3Byb3Bvc2ljYW8vBl9ibGFuaxxQcm9wb3Npw6fDtWVzIGRvIExlZ2lzbGF0aXZvZAIPD2QWAmYPFQMzaHR0cDovL3d3dy5sZWlzbXVuaWNpcGFpcy5jb20uYnIvY2FtYXJhL2JhL3NhbHZhZG9yBl9ibGFuaw9MZWlzIE11bmljaXBhaXNkAhAPZBYCZg8VA3BodHRwOi8vMTc3LjEzNi4xMjMuMTUzL2Zvcm0uanNwP3N5cz1TQVAmYWN0aW9uPW9wZW5mb3JtJmZvcm1JRD04MzI0JmFsaWduPTAmbW9kZT0tMSZnb3RvPS0xJmZpbHRlcj0mc2Nyb2xsaW5nPW5vBl9ibGFuaxtBY29tcGFuaGFtZW50byBkZSBQcm9jZXNzb3NkAhEPZBYCZg8VAzBodHRwOi8vMTc3LjEzNi4xMjMuMTQ5L2V4dC8/Z2V0PXJlY3Vyc29zX2h1bWFub3MGX2JsYW5rEFJlY3Vyc29zIEh1bWFub3NkAhIPZBYCZg8VAw9yZWxhdG9yaW9zLmFzcHgAD1JlbGF0w7NyaW9zIExSRmQCAw8WAh8EAgUWCmYPZBYCZg8VAyNodHRwOi8vMTc3LjEzNi4xMjMuMTQ4L3B1Yi9ET0wtNTI3MRtDYXBhXzIwMTg3MTE4NDAyOTk3MjEzNC5qcGcKMTEvMDcvMjAxOGQCAQ9kFgJmDxUDI2h0dHA6Ly8xNzcuMTM2LjEyMy4xNDgvcHViL0RPTC01MjcwH0NhcGFfNTI3MF8yMDE4NzEwODcxNzM5ODYxMy5qcGcKMTAvMDcvMjAxOGQCAg9kFgJmDxUDI2h0dHA6Ly8xNzcuMTM2LjEyMy4xNDgvcHViL0RPTC01MjY5HkNhcGFfNTI2OV8yMDE4Nzk4MzU0MTQ1MjE0LmpwZwowOS8wNy8yMDE4ZAIDD2QWAmYPFQMjaHR0cDovLzE3Ny4xMzYuMTIzLjE0OC9wdWIvRE9MLTUyNjgfQ2FwYV81MjY4XzIwMTg3NjkzNzM0OTY5NzA4LmpwZwowNi8wNy8yMDE4ZAIED2QWAmYPFQMjaHR0cDovLzE3Ny4xMzYuMTIzLjE0OC9wdWIvRE9MLTUyNjcfQ2FwYV81MjY3XzIwMTg3NTc1NjU5Mzg3NjkyLmpwZwowNS8wNy8yMDE4ZAIFDw8WAh4ISW1hZ2VVcmwFIGh0dHA6Ly93d3cuY21zLmJhLmdvdi5ici91cGxvYWQvZGQCBw8WAh4EVGV4dAXdAjxwPjxzdHJvbmc+QXNzZXNzb3JpYSBkZSBDb211bmljYSZjY2VkaWw7JmF0aWxkZTtvPC9zdHJvbmc+IFRlbC46ICg1NSA3MSkgMzMyMC0wMjA1PGJyIC8+DQpUZWxlZmF4OiAoNTUgNzEpIDMzMjAtMDM4MDxiciAvPg0KZS1tYWlsOiBpbXByZW5zYS5jbXNAY21zLmJhLmdvdi5icjxiciAvPg0KJm5ic3A7Jm5ic3A7Jm5ic3A7IGltcHJlbnNhY21zQGdtYWlsLmNvbTxiciAvPg0KPGJyIC8+DQo8c3Ryb25nPkFzc2Vzc29yaWEgZGUgSW5mb3JtJmFhY3V0ZTt0aWNhPC9zdHJvbmc+IFRlbC46ICg1NSA3MSkgMzMyMC0wMTQzPGJyIC8+DQplLW1haWw6IGFzc2luQGNtcy5iYS5nb3YuYnI8YnIgLz4NCiZuYnNwOzwvcD5kAgsPFgIfBgWCBjxwPjxzdHJvbmc+Q29udGF0bzwvc3Ryb25nPnh4eCBQcmEmY2NlZGlsO2EgVGhvbSZlYWN1dGU7IGRlIFNvdXphLCBzL24mb3JkbTssJm5ic3A7Q2VudHJvPC9wPg0KPHA+Q2VwLiA0MC4wMjAtMDEwIFNhbHZhZG9yIC0gQmFoaWEgLSBCcmFzaWw8L3A+DQo8cD5UZWwuOiArNTUgKDcxKSAzMzIwLTAxMTYmbmJzcDsgPHNwYW4gc3R5bGU9ImNvbG9yOiByZ2IoMjU1LCAwLCAwKTsiPiZsdDticiZndDsgQWJlcnRhIGFvIHAmdWFjdXRlO2JsaWNvOiBTZWd1bmRhIGEgc2V4dGEsIGRhcyA4aCAmYWdyYXZlO3MgMTJoIGUgZGFzIDE0aCAmYWdyYXZlO3MgMThoPC9zcGFuPjwvcD4NCjxwPjxzcGFuIHN0eWxlPSJjb2xvcjogcmdiKDI1NSwgMCwgMCk7Ij4mbmJzcDs8L3NwYW4+PC9wPg0KPHA+PGEgdGFyZ2V0PSJibGFuayIgaHJlZj0iaHR0cDovL21hcHMuZ29vZ2xlLmNvbS9tYXBzP2Y9cSZhbXA7c291cmNlPXNfcSZhbXA7aGw9cHQtQlImYW1wO2dlb2NvZGU9JmFtcDtxPWMmYWNpcmM7bWFyYStkb3MrdmVyZWFkb3JlcytkZStzYWx2YWRvcitiYWhpYSticmFzaWwmYW1wO3NsbD0zNy41MDk3MjYsLTk1LjcxMjg5MSZhbXA7c3Nwbj01MC4zOTc5OCw3OS4xMDE1NjMmYW1wO2llPVVURjgmYW1wO2ZpbHRlcj0wJmFtcDt1cGRhdGU9MSZhbXA7bGw9LTEyLjk3MTc3MywtMzguNTEzNDY0JmFtcDtzcG49MC4wMDc2NzQsMC4wMDk2NTYmYW1wO3o9MTciPjxpbWcgYWx0PSIiIHNyYz0iaW1hZ2VzL2dvb2dsZV9tYXBzLmpwZyIgYWxpZ249InJpZ2h0IiAvPjwvYT48L3A+ZBgCBSNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGRwTm90aWNpYQ8UKwAEZAIQAgQCsgFkBSNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGx2Tm90aWNpYQ8UKwAOZGRkZGRkZDwrAAQAArIBZGRkAhACBGQiPIJ6EjIkeuB2082RW2i3bhhO284mOdjI69F2UiDIPQ=='
init_eventValidation = '/wEdAFxr7HwBFN6Hx7W0srxRTCS1Yf0n62fyYZzGaAXs4UYW1wkf9rwsatGNCE30dSWXZeBQy2iPeylGGJVSOnqEswik0Wuv+68V0exrp51TYhifSPIMtpLrdPAOunIiCr0lKI4GQPmYJULQm8EdSacoxsWkjf4oZAj9gk06elS4iI0iwwt+ZtO9kU0Vq4e1rQE8QKbXdSiZCgKoC95zh/6ayYUmILZ19241R2sETSBJS42iVYEZOku6ckEtQA9YG0YDp0OpLODaAmEwY2q/qFyW/j2dqM+P8B9igmH/ITutnlZGMEV5OdvMx1UxntqfQHTZmCK94n18og4Q1AWGNF8PsV8f9L382tiCYlRVcVGic7y1/0WOttqYmqJ4fnulztB0Vr/9km1s4hGb2PIhvz3nNIowVH8+0XIUOhSmsL/phN4MR4LpJVDHPa+WVPD4ayTuByHsQ/lUvK+EdlSBQwW55VtquTDicVhUnub4sYmr4Brzk7ZvKm011U1a6hbUvNeVGGwbw9XKNtxqb8/c6kscl6n1Rfy++IHa1vFL+XV+bMMrEa8hkuhBugPzCSET7MPGhe6nR6edLumxfD8X665dNQbuGsH6pFF52Mfo8Odp7J6d+GkRKBHW5MYHfwKYf41F9Y8i7fwN1u7bqTUCTffEV5XI2PUnpc3nkOMcGqNVn005yhiuqItaWEtpIs3xoAtecgezGK79DCuJfJ9GElOJP4YRF1F6BUUgVL8/5G/RZUR9RWlQ/zP/ckM6R6cL47dDYhjrwaevYgt0XETnZV6xu5QtElq4JmLSqKZ3PdeUzL1iJivJ5acwIkVdVJgcKaHcCty6udre24lCyWCuK6ib7azufM4eDcI4r4U6TcojZoDyVi5fnfVaytXGYrHCsTkhwcAdc87U3PTbQwZzK9wvYghsgpl6YaNxAufQ9gX/LgZD7AsvR5kGUgZDftzbwX8kCRJRlNyTEdBekwPp2UvFkJ64P6PFAdMmnrlk0QnZLxBad6Fm95dLpWVTRfvUFHeriWwXm7eJEitPcm+9s5sU23gZoPF9jSq81sVFa3rLIixERe0SBThq0Q3M7jcj6fHiqF47EjI3TIm53ccJVxm/Dvz26trsu9V69trQe61ySso3sbTBjbqGpEdAuuxuvajswZplmivPvcVec89RXO+RBBNYEf6+ZeqQHoauKLRhqv8TFWaZ/X+06ay5IE2IwG2W50+qs955cL403oFx9tVjM5e5Zj97WhLBS07Ohm2EkJdlbBWLwwcS+sA9xuKqBWOYhDGhMAkWFSgpE7TgThEtfs5O6CxbJYHwv7eBX1SkUWbJExa8vliIXqO2xJl8jv5+RaHMWZA5jh87UadWzUZsA2Oq2KIQ++IXqb7k6lKNXzzDDKy4H2ol/jDf1P+1yaVQ3poIyTfQUsYLI3IALysEzbzENZmG2jEldFLlRnHj/RhgUHG3nhHPWnfAi2FajdGXcCqp1uavDJRHU/kdHVSZWNK4f+PmsmRgdUdqG8lvTzfF3VoewZUAY4SS2LJsK7mCD7G1gcZjsiGvWnIyQPnAmOoGHDzTFedFXbG9venSOLlw68XYcC5vNDKVH5Te5BpTiKiq97KoCipdGJiGX/P0858i0sTP6pGe9ZmXXjoxoStTC60JNGI6h83RQynoo82SA52KNeLLd6ScXWa/aIEes8PixFd9jp49nMhHwe904pX3W96OvwNuQ1Dxf5VVp6KlaRZM1BLiAO/QDwjAZqhVyTQ5e+4OT1llddikeL5jgpPYU1XV/zLAEHLI+V4gtXlfUvVrXynajUz+hVkHjViFG+XZtQw65QGS8YpXMjKeZTrZFz6+bHtDEVROJEI2DvaalL6q6rPfNQdX9rzsLby+YfDH/vWoyZ8AJImDcT+zdO4pUvHQBLfAVT+VspH+b9KUUKLxn8rUjISlxkqk5AW11NNVxUPwnt8bG8ocU57oz58oGA6LWO6H+qUeLmIYUTxcLv29t4eIIwOOYj+oFQDclHYn'

def pagina( viewState, eventValidation, pagina ):
	indice = pagina%11

	if pagina > 10:
		indice += 1

	print( ' ** Pagina ' + str( pagina ) + ' Indice ' + str( indice ) )
	strIndice = str( indice )
	temProxima = False
	strListaPaginas = ''

	if len( strIndice ) == 1:
		strIndice = '0'+strIndice

	dados = {
		'ctl00$ContentPlaceHolder1$ToolkitScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$dpNoticia$ctl01$ctl'+strIndice,
		'__EVENTTARGET': 'ctl00$ContentPlaceHolder1$dpNoticia$ctl01$ctl'+strIndice,
		'__VIEWSTATEGENERATOR': '48B4125A',
		'__EVENTVALIDATION': eventValidation,
		'__VIEWSTATE': viewState
	}

	r = requests.post( 'http://www.cms.ba.gov.br/despesa.aspx', data=dados )
	print( r.text )
	parsed_html = BeautifulSoup( r.text, 'html.parser' )
	novo_viewState = parsed_html.body.find('input', attrs={'id':'__VIEWSTATE'})["value"]
	novo_eventValidation = parsed_html.body.find('input', attrs={'id':'__EVENTVALIDATION'})["value"]
	conteudo = parsed_html.body.find('div', attrs={'id':'ContentPlaceHolder1_UpdatePanel1'})
	paginador = parsed_html.body.find('span', attrs={'id':'ContentPlaceHolder1_dpNoticia'})
	paginaAtual = paginador.find('span').text
	tagsA = paginador.find_all('a')

	for link in tagsA:
		strListaPaginas += link.text + ' '

		if not temProxima:
			if link.text.isnumeric() == True & paginaAtual.isnumeric() == True & int( link.text ) > int( paginaAtual ):
				temProxima = True

			elif link.text == '...':
				temProxima = True


	return ({
		'temMais': temProxima,
		'paginas': strListaPaginas,
		'paginaAtual': paginaAtual,
		'viewState': novo_viewState,
		'eventValidation': novo_eventValidation
	})

viewState = init_viewState
eventValidation = init_eventValidation

for pag in range( 10 ):
	retorno = pagina( init_viewState, init_eventValidation, pag )

	print( ' ** HTML ' + retorno['paginaAtual'] )
	print( ' ** Lista ' + retorno['paginas'] )
	print( '-'*100 )

	if retorno['temMais'] != True:
		break

	viewState = retorno['viewState']
	eventValidation = retorno['eventValidation']
	time.sleep( 1 )